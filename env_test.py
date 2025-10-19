import sys, inspect
import mesa
print("mesa file:", inspect.getfile(mesa))
print("mesa version:", getattr(mesa, "__version__", "unknown"))
print("sys.path[0]:", sys.path[0])
python -V                      # 应该是 Python 3.10.10
pip show mesa                 # 应该能看到版本 2.4.0 与 site-packages 路径
python -c "import mesa; import inspect; import importlib.util as u; import sys; import os; print(mesa.__version__, inspect.getfile(mesa))"
