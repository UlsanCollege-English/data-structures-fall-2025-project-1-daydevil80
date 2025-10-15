import sys
import os

# Add project root to Python path
project_root = os.path.abspath(os.path.join(os.getcwd()))
sys.path.insert(0, project_root)

from src.scheduler import Scheduler
