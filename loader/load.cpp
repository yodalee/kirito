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
string OUTPUT("trace_cpp.npy");

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

// load dir, read every file into a big large vector
int loaddir(string path) {
  vector<int16_t> data;
  uint64_t row = 0;
  uint64_t col = 0;

  // list directory and sort it
  vector<string> filelist = listdir(path.c_str());
  sort(filelist.begin(), filelist.end());

  // skip if list is empty
  row = filelist.size();
  if (row == 0) {
    return EXIT_FAILURE;
  }

  // preload, reserve space for data
  auto preload = loadfile(filelist[0].c_str());
  col = preload.size();
  data.reserve(row * col);

  // iterator filelist
  for (auto s: filelist) {
    auto load = loadfile(s.c_str());
    data.insert(data.end(), load.cbegin(), load.cend());
  }
  cnpy::npy_save(OUTPUT, &data[0], {row, col}, "w");

  return EXIT_SUCCESS;
}

int main(int argc, char *argv[])
{
  int ret = loaddir(LOGDIR);
  return ret;
}
