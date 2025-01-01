from setuptools import setup

package_name = 'light_source'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Light source publisher for Turtlesim',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'light_publisher = light_source.light_publisher:main',
            'light_indicator = light_source.light_indicator:main',
        ],
    },
)
