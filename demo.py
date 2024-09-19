import sys, threading
python_version = '311'

if python_version == '311':
    import importlib
    def import_pyc(module_name, pyc_file_path):
        spec = importlib.util.spec_from_file_location(module_name, pyc_file_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
else:
    import importlib.util as iu
    def import_pyc(module_name, pyc_file_path):
        spec = iu.spec_from_file_location(module_name, pyc_file_path)
        module = iu.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
##################################################################################

# Paths to the .pyc files
com_barcode_pyc_path   = f'__pycache__/com_barcode.cpython-{python_version}.pyc'
# Import the .pyc files
com_barcode = import_pyc("com_barcode", com_barcode_pyc_path)
BarcodeScanner = com_barcode.BarcodeScanner
##################################################################################

def thread_class(scanner):
    scanner.start()
    return

if __name__ == "__main__":
    baudrate = 9600
    scanner = BarcodeScanner(baudrate)
    t = threading.Thread(target=thread_class, args=(scanner,), daemon=True)
    t.start()

    while True:
        barcode = scanner.get_barcode()
        detailBarcode = scanner.get_barcodeDetailed()
        if barcode != None and detailBarcode != {}:
            print(f"-----> {barcode}")
            print(f"-----> {detailBarcode}")
        threading.Event().wait(.1)