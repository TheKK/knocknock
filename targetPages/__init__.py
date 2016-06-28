import pkgutil

all_pages = []

for loader, module_name, is_pkg in  pkgutil.walk_packages(__path__):
    module = loader.find_module(module_name).load_module(module_name)
    all_pages.append(module.Target_page())
