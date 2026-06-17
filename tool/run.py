
import flags
import logging
import platform
import multiprocessing
from absl import app
from utils import log_util
from modules import MODULES

FLAGS = flags.FLAGS


def _print_all_flags():
  for module_name, flag_obj_list in FLAGS.flags_by_module_dict().items():
    # 只打印 flags 模块的参数，其他模块的参数不打印
    if module_name != "flags":
      continue

    logging.info(f"===== 模块: {module_name} =====")
    for flag_obj in flag_obj_list:
      flag_name = flag_obj.name
      val = getattr(FLAGS, flag_name)
      logging.info(f"参数: --{flag_name}")
      logging.info(f"  默认值: {flag_obj.default}")
      logging.info(f"  当前值: {val}")

# def _CreateBenchmarkSpecs():
#   """Create a list of specs for each  run to be scheduled."""
#   resources.LoadModules()
#   specs = []
#   benchmark_tuple_list = benchmark_sets.GetBenchmarksFromFlags()
#   benchmark_counts = collections.defaultdict(itertools.count)
#   for benchmark_module, user_config in benchmark_tuple_list:
#     # Construct benchmark config object.
#     name = benchmark_module.BENCHMARK_NAME
#     # This expected_os_type check seems rather unnecessary.
#     expected_os_types = os_types.ALL
#     with flag_util.OverrideFlags(FLAGS, user_config.get('flags')):
#       config_dict = benchmark_module.GetConfig(user_config)
#     config_spec_class = getattr(
#         benchmark_module,
#         'BENCHMARK_CONFIG_SPEC_CLASS',
#         benchmark_config_spec.BenchmarkConfigSpec,
#     )
#     config = config_spec_class(
#         name,
#         expected_os_types=expected_os_types,
#         flag_values=FLAGS,
#         **config_dict,
#     )

#     # Assign a unique ID to each benchmark run. This differs even between two
#     # runs of the same benchmark within a single PKB run.
#     uid = name + str(next(benchmark_counts[name]))

#     # Optional step to check flag values and verify files exist.
#     check_prereqs = getattr(benchmark_module, 'CheckPrerequisites', None)
#     if check_prereqs:
#       try:
#         with config.RedirectFlags(FLAGS):
#           check_prereqs(config)
#       except:
#         logging.exception('Prerequisite check failed for %s', name)
#         raise

#     with config.RedirectFlags(FLAGS):
#       specs.append(
#           bm_spec.BenchmarkSpec.GetBenchmarkSpec(benchmark_module, config, uid)
#       )

#   return specs

def Runs():
  """Start Run."""
  # specs = _CreateSpecs()
  logging.info(f"Running benchmarks: {MODULES}")
  return 0


# 自定义主函数
def main(argv):
  del argv  # Unused.

  # macOS 上默认的 multiprocessing 启动方式是 'spawn'，但在某些情况下可能会导致问题。
  # 强制使用 'fork' 启动方式，适用于大多数 Unix-like 系统。
  if platform.system() == 'Darwin':
    multiprocessing.set_start_method('fork', force=True)

  # 配置Logging
  log_util.ConfigureLogging()

  # 打印flags
  #_print_all_flags()
  
  print(__name__)

  return Runs()

if __name__ == "__main__":
    # 运行主函数，使用默认参数解析
    app.run(main)

