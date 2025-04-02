from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Layer(_message.Message):
    __slots__ = ("layer_index",)
    LAYER_INDEX_FIELD_NUMBER: _ClassVar[int]
    layer_index: int
    def __init__(self, layer_index: _Optional[int] = ...) -> None: ...

class ActivationFloat(_message.Message):
    __slots__ = ("data", "shape_f")
    DATA_FIELD_NUMBER: _ClassVar[int]
    SHAPE_F_FIELD_NUMBER: _ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[float]
    shape_f: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, data: _Optional[_Iterable[float]] = ..., shape_f: _Optional[_Iterable[int]] = ...) -> None: ...

class ActivationByte(_message.Message):
    __slots__ = ("buffer", "shape_b", "dtype")
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    SHAPE_B_FIELD_NUMBER: _ClassVar[int]
    DTYPE_FIELD_NUMBER: _ClassVar[int]
    buffer: bytes
    shape_b: _containers.RepeatedScalarFieldContainer[int]
    dtype: str
    def __init__(self, buffer: _Optional[bytes] = ..., shape_b: _Optional[_Iterable[int]] = ..., dtype: _Optional[str] = ...) -> None: ...
