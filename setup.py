from setuptools import setup

with open('requirements.txt') as fp:
    requirements = fp.read().splitlines()

setup(
    name='Blacksheep-RateLimiter',
    author='Concord',
    url='https://github.com/concordchat/Blacksheep-RateLimiter',
    version='1.0.6',
    packages=['blacksheep_ratelimiter'],
    license='MIT',
    description='RateLimit Middleware for Blacksheep',
    install_requires=requirements,
    python_requires='>=3.9',
    include_package_data=True
)
