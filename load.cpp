#include <iostream>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>

#include <dirent.h>
#include "cnpy.h"

using std::vector;
using std::string;

string LOGDIR("trace/");

vector<int16_t> loadfile(string file) {
  std::cout << LOGDIR + file << std::endl;
  std::ifstream ifs(LOGDIR + file);
  int16_t value;
  vector<int16_t> data;
  while (ifs >> value) {
    data.push_back(value);
  }
  return data;
}

vector<string> listdir(const char *path) {
  DIR *dir;
  struct dirent *ent;
  vector<string> filelist;
  if ((dir = opendir(path)) != NULL) {
    while ((ent = readdir(dir)) != NULL) {
      if (ent->d_type == DT_REG) {
        filelist.push_back(ent->d_name);
      }
    }
    closedir(dir);
  } else {
    perror("");
    exit(EXIT_FAILURE);
  }
  return filelist;
}

vector<vector<int16_t>> loaddir(string path) {
  vector<vector<int16_t>> data;
  vector<string> filelist = listdir(path.c_str());
  sort(filelist.begin(), filelist.end());
  for (auto s: filelist) {
    data.push_back(loadfile(s.c_str()));
  }
  return data;
}

int main(int argc, char *argv[])
{
  auto data = loaddir(LOGDIR);

  return 0;
}
