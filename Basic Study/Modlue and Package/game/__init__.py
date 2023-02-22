# 현재 폴더가 패키지임을 알리는 초기화 스크립트
# 3.3+ 부터는 안해도 되지만,해야됨(?)

__all__ = ["image","sound","stage"]

# .을 사용하면 현재 디렉토리 기준
from . import image
from . import sound
from . import stage