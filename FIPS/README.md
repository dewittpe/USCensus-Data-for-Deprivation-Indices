# FIPS Reference Data

## Notes

- Connecticut county equivalents changed in the Census Bureau geography:
  the state adopted nine Councils of Governments (planning regions) as the
  county-equivalent units, replacing the prior county list in newer years.
- Tract differences between `2020__tracts.csv` and `2022__tracts.csv` are
  entirely in Connecticut and are a direct consequence of the county-equivalent
  change above. After normalizing name punctuation, there are no other tract
  changes between those years.
- Tract differences between `2022__tracts.csv` and `2023__tracts.csv` are
  limited to New York (state `36`), with 15 tracts present in 2022 but not 2023,
  all in Suffolk County (`103`).
- Block group differences between 2020 and 2021/2022 are large and expected:
  2020 uses the older county framework (pre-CT planning regions), while
  2021/2022 reflect the updated geography. The differences are spread across
  48 states, with California, Texas, New York, Florida, and Pennsylvania having
  the largest counts. 2021 and 2022 block groups match each other.
- Block group differences between 2022 and 2023 are small: 42 block groups
  present in 2022 are absent in 2023, all in New York (state `36`), Suffolk
  County (`103`), matching the tract-level changes noted above.

### Citations

- U.S. Census Bureau, County Changes (Connecticut county-equivalent update).
  https://www.census.gov/programs-surveys/geography/technical-documentation/county-changes.html
- U.S. Census Bureau PDF: Final Change to County Equivalents in Connecticut.
  https://www2.census.gov/geo/pdfs/reference/ct_county_equiv_change.pdf
- Federal Register notice: Change to County Equivalents in the State of
  Connecticut. https://www.federalregister.gov/documents/2022/06/06/2022-12063/change-to-county-equivalents-in-the-state-of-connecticut
