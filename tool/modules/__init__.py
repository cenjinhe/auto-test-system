import os
import importlib.util
from typing import Generator, List

def _LoadBenchmarks():
  """加载当前包目录下所有模块文件"""
  package_dir = __path__[0]
  package_name = __name__
  modules = []

  for filename in os.listdir(package_dir):
      file_path = os.path.join(package_dir, filename)
      # 只处理 .py 文件，跳过文件夹
      if not filename.endswith(".py") or os.path.isdir(file_path):
        continue
      # 跳过自身 __init__.py
      if filename == "__init__.py":
        continue

      # 去掉后缀 .py
      mod_base_name = filename[:-3]
      # full_mod_name = f"{package_name}.{mod_base_name}"

      # 动态导入模块
      spec = importlib.util.spec_from_file_location(mod_base_name, file_path)
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)
      modules.append(module)

  return modules


# 执行加载，得到当前包下所有导入后的模块对象
ALL_FILES = _LoadBenchmarks()
MODULES = []

VALID_MODULES = {}
for module in ALL_FILES:
  # 只保留文件名以 _benchmark 结尾的基准测试模块
  name = module.__name__
  if name.endswith('_benchmark'):
    # 判断该名称是否已经存在，重名直接抛异常
    if name in VALID_MODULES:
      raise ValueError(
        'There are multiple modules with module name "%s"'
        % (name)
      )

    MODULES.append(module)
    VALID_MODULES[name] = module

