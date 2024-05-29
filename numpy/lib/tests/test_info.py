import numpy as np
import pytest

info = np.__array_namespace_info__()

def test_capabilities():
    caps = info.capabilities()
    assert caps["boolean indexing"] == True
    assert caps["data-dependent shapes"] == True
    assert caps["max rank"] == 32

def test_default_device():
    assert info.default_device() == 'cpu'

def test_default_dtypes():
    dtypes = info.default_dtypes()
    assert dtypes["real floating"] == np.float64
    assert dtypes["complex floating"] == np.complex128
    assert dtypes["integral"] == np.int64
    assert dtypes["indexing"] == np.int64

    with pytest.raises(ValueError, match='Device not understood'):
        info.default_dtypes(device='gpu')

def test_dtypes_all():
    dtypes = info.dtypes()
    assert dtypes == {
        "bool": np.bool_,
        "int8": np.int8,
        "int16": np.int16,
        "int32": np.int32,
        "int64": np.int64,
        "uint8": np.uint8,
        "uint16": np.uint16,
        "uint32": np.uint32,
        "uint64": np.uint64,
        "float32": np.float32,
        "float64": np.float64,
        "complex64": np.complex64,
        "complex128": np.complex128,
    }

@pytest.mark.parametrize("kind,expected", [
    ("bool", {"bool": np.bool_}),
    ("signed integer", {
        "int8": np.int8,
        "int16": np.int16,
        "int32": np.int32,
        "int64": np.int64
    }),
    ("unsigned integer", {
        "uint8": np.uint8,
        "uint16": np.uint16,
        "uint32": np.uint32,
        "uint64": np.uint64,
    }),
    ("integral", {
        "int8": np.int8,
        "int16": np.int16,
        "int32": np.int32,
        "int64": np.int64,
        "uint8": np.uint8,
        "uint16": np.uint16,
        "uint32": np.uint32,
        "uint64": np.uint64,
    }),
    ("real floating", {"float32": np.float32, "float64": np.float64}),
    ("complex floating", {"complex64": np.complex64, "complex128": np.complex128}),
])
def test_dtypes_kind(kind, expected):
    assert info.dtypes(kind=kind) == expected

def test_dtypes_tuple():
    dtypes = info.dtypes(kind=("bool", "integral"))
    assert dtypes == {
        "bool": np.bool_,
        "int8": np.int8,
        "int16": np.int16,
        "int32": np.int32,
        "int64": np.int64,
        "uint8": np.uint8,
        "uint16": np.uint16,
        "uint32": np.uint32,
        "uint64": np.uint64,
    }

def test_dtypes_invalid_kind():
    with pytest.raises(ValueError, match="unsupported kind"):
        info.dtypes(kind="invalid")

def test_dtypes_invalid_device():
    with pytest.raises(ValueError, match='Device not understood'):
        info.dtypes(device='gpu')

def test_devices():
    assert info.devices() == ['cpu']
