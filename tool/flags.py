
"""File used for the management of flags."""

import getpass
from absl import flags

MAX_RUN_URI_LENGTH = 12
FLAGS = flags.FLAGS


def GetCurrentUser():
  """Get the current user name.
  Returns:
    User name OR default string if user name not available.
  """
  try:
    return getpass.getuser()
  except KeyError:
    return 'user_unknown'


flags.DEFINE_string(
    'owner',
    GetCurrentUser(),
    'Owner name. Used to tag created resources and performance records.',
)

flags.DEFINE_integer(
    'run_processes',    # 1. 参数名：命令行使用 --run_processes
    None,               # 2. 默认值：不传参时为 None
    'The number of parallel processes to use to run benchmarks.',   # 3. 参数说明（help 文档）
    lower_bound=1,      # 4. 数值下限：要求输入必须 ≥1，小于1会直接报错
)
