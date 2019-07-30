import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='drf_response',
     version='0.1',
     scripts=['drf_response'] ,
     author="Raisul Islam",
     author_email="raisul@kutumbita.com",
     description="A custom package for drf reponse",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/raisulkutumbita/drf_response",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )