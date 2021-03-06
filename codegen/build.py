import jinja2

TEMPLATE_PATH = "./"
SRC_PATH = "../src/com/vladris/maki"
SRC_DETAILS_PATH = f"{SRC_PATH}/details"
TEST_PATH = "../test/com/vladris/maki"

templates = {
    "TypeGuard.java": SRC_DETAILS_PATH,
    "Variant.java": SRC_PATH,
    "VariantTest.java": TEST_PATH,
}

for file in templates:
    templateLoader = jinja2.FileSystemLoader(searchpath=TEMPLATE_PATH)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(f"{file}.template")

    for i in range(1, 9):
        fileName, ext = file.split(".")

        if fileName.endswith("Test"):
            fileName, suffix = fileName[0:-4], "Test"
        else:
            suffix = ""

        with open(f"{templates[file]}/{fileName}{i}{suffix}.{ext}", "w") as f: 
            f.writelines(template.render(types=i))