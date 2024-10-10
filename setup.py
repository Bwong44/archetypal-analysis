from pathlib import Path
from setuptools import find_packages, setup

setup(
    name='archetypal-analysis-popgen',
    version='0.1.0',
    long_description=(Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    description='Archetypal Analysis for Population Genetics',
    url='https://github.com/AI-sandbox/archetypal-analysis',
    author='Júlia Gimbernat-Mayol',
    author_email='juliagimbernat@gmail.com',
    entry_points={
        'console_scripts': ['archetypal-analysis=entry:main', 'archetypal-plot=entry:plot']
    },
    license='CC BY-NC 4.0',
    packages=find_packages('archetypal_analysis/')+['.'],
    package_dir={"": "archetypal_analysis"},
    python_requires=">=3.10.0",
    install_requires=["matplotlib==3.9.2",
                      "numpy==2.0.2",
                      "pandas==2.2.3",
                      "pandas-plink==2.2.9",
                      "plotly==5.24.1",
                      "scikit-allel==1.3.13",
                      "scikit-learn==1.5.2",
                      "scipy==1.14.1",
                      "umap-learn==0.5.6"
                      ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
    ],
)
