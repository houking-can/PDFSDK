# PDFSDK
Based on [Foxit Quick PDF Library](https://www.debenu.com/products/development/debenu-pdf-library/)，python interface.

# Introduction

Foxit Quick PDF Library is a popular SDK for working with PDF documents.

The files in this repository contain classes that make it as easy as possible to control Quick PDF Library using the Python programming language. Interface classes are provided for Windows (DLL), macOS (Dylib) and Linux (.so shared library).

# How to use it

- Download the corresponding Foxit Quick PDF Library version

```python
# On Windows use FoxitQPLDLL1611, on macOS use FoxitQPLmacOS1611 and on Linux use FoxitQPLLinux1611
import FoxitQPLDLL1611 as FoxitQuick

# Create an instance of the class
# No parameter is supplied so the script will look for the QPL binary in the same directory
qp = FoxitQuick.PDFLibrary()
licenseKey = "..."
if qp.UnlockKey(licenseKey) == 1:
  qp.DrawText(100, 700, "Hello world")
  qp.SaveToFile("test_output.pdf")
```

# API

Foxit Quick PDF Library 17.11 Reference Guide.pdf