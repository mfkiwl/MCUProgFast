import collections

from . import STM32F103
from . import STM32F405

Devices = collections.OrderedDict([
    ('STM32F103C8', STM32F103.STM32F103C8),
    ('STM32F103RC', STM32F103.STM32F103RC),
    ('STM32F405RG', STM32F405.STM32F405RG)
])