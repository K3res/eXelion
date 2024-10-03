from setuptools import setup, find_packages


setup(
    name="exelion",  
    version="0.5.0", 
    description="Tools for XXE/XEE Payloads and Crawling",  
    author="K3res",   
    url="https://github.com/K3res/eXelion",  
    packages=find_packages(), 
    install_requires=[ 
        "requests",
        "beautifulsoup4",
        "urllib3",
        "colorama"
       
           ],
    entry_points={  
        'console_scripts': [
            'exelion=eXelion:main',  
        ],
    },
    classifiers=[ 
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  
)
