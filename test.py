import sys
from src.exception import CustomException

try:
    # Intentionally causing a Division by Zero error
    result = 1 / 0
except Exception as e:
    raise CustomException(e, sys)