import setuptools

setuptools.setup(name='GenerateMapImage',
      version='0.6.1',
      description='Generate an image of a map based on dataframe with latitude and longitude coordinates',
      author='Mike Bromberek',
      license='BSD 3-Clause License',
      packages=['GenerateMapImage'],
      install_requires=['numpy','pandas','plotly','kaleido']
)
