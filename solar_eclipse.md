---
layout: null
permalink: /:city/
---
{% assign city_data = site.data.solar_eclipse_data | where: "city", page.city | first %}
{% if city_data %}
Gerhana di {{ city_data.city | capitalize }} akan memiliki presentase {{ city_data.data1 }}%, starting at {{ city_data.data2 }}, maximum at {{ city_data.data3 }}, end at {{ city_data.data4 }}.
{% else %}
Sorry, we don't have data for the specified city.
{% endif %}
