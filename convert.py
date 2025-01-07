import sys
import pypandoc


def main(file_name: str):
    # file should be a markdown file
    if not file_name.endswith(".md"):
        raise ValueError("File should be a markdown file")

    output_file = file_name.replace(".md", ".html")

    # convert markdown to html with pandoc
    pypandoc.convert_file(
        file_name,
        "html",
        outputfile=output_file,
        extra_args=[
            "--template=./templates/newcss.html",
            "--toc",
            "--embed-resources",
            "--standalon",
        ],
    )


if __name__ == "__main__":
    file_name = sys.argv[1]
    main(file_name)
