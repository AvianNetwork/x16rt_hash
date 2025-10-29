#define PY_SSIZE_T_CLEAN

#include <Python.h>

#include "x16rt.h"

static PyObject *x16rt_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
    PyBytesObject *input;

    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

    x16rt_hash((char *)PyBytes_AsString((PyObject *)input), output);

    Py_DECREF(input);
    value = Py_BuildValue("y#", output, 32);
    PyMem_Free(output);
    return value;
}

static PyMethodDef X16RTMethods[] = {
    {"getPoWHash", x16rt_getpowhash, METH_VARARGS, "Returns the proof of work hash using X16RT hash"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef X16RTModule = {
    PyModuleDef_HEAD_INIT,
    "x16rt_hash",
    "Python bindings for the x16rt hash function used in Veil cryptocurrency PoW",
    -1,
    X16RTMethods};

PyMODINIT_FUNC PyInit_x16rt_hash(void)
{
    return PyModule_Create(&X16RTModule);
}
