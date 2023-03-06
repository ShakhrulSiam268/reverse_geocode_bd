# Reverse GeoCode BD

[//]: # ([![PyPI Downloads]&#40;https://static.pepy.tech/personalized-badge/reverse-geocode-bd?period=total&units=international_system&left_color=grey&right_color=blue&left_text=pypi%20downloads&#41;]&#40;https://pepy.tech/project/reverse-geocode-bd&#41;)

## Installation
```shell
$ pip install reverse-geocode-bd
```
A Python library for offline reverse geocoding. Reverse Geocode BD takes a (latitude , longitude) coordinate and returns the Division, District, Upazila and Thana of any location in Bangladesh.

##  Example Use 
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

