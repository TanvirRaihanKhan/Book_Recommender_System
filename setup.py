from setuptools import setup
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()

# Edit below varialbles as per requirements
REPO_NAME="Books-Recommender_System-Using-Machine-Learning"
AUTHOR_USER_NAME="TanvirKhan"
SRC_REPO="src"
LIST_OF_REQUIREMENTS=['stramlit','numpy']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_USER_NAME,
    description="A small package for Book Recommender System",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="khantanvirraihan@gmail.com",
    packages=SRC_REPO,
    license="MIT",
    install_requires=LIST_OF_REQUIREMENTS
)

