# Reverse GeoCode BD

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/reverse-geocode-bd?period=month&units=international_system&left_color=blue&right_color=orange&left_text=PyPi%20Downloads)](https://pepy.tech/project/reverse-geocode-bd)

## Installation
```shell
$ pip install reverse-geocode-bd
```
A Python library for offline reverse geocoding. Reverse Geocode BD takes a (latitude , longitude) coordinate and returns the Division, District, Upazila and Thana of any location in Bangladesh.

Package Available at : https://pypi.org/project/reverse-geocode-bd/

##  Uses Example
```python
from reverse_geocode_bd import ReverseGeoBD

loc = ReverseGeoBD()
loc.find(25.7363, 89.2715)

```
Or

```python
import reverse_geocode_bd

reverse_geocode_bd.search(25.7363, 89.2715)

```

### Output
```json
{'division': 'Rangpur',
 'district': 'Rangpur',
 'upazila': 'Rangpur Sadar',
 'union': 'Paurashava'}
```

