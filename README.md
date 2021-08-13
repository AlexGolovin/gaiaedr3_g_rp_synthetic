# gaiaedr3_g_rp_synthetic
This tool calculates synthetic (or "deblended") G-RP for datasets from *Gaia* eDR3 using BP-RP photometry as input observable.
The details of this method are described in [Golovin et al. 2021, A&A, [...]]().

### Input
The input is a fits-file with dataset from *Gaia* eDR3. BP-RP colour values are stored in the column with the default name `bp_rp`. If you need to rename the column, you can do it by adding the following line after you loaded the input file:
```python
input_table.rename_column('your_bp_rp_column_name', 'bp_rp')
```


Please be reminded that the initial purpose of this tool was to be applied on the sample of nearby stars  (*d* ≤ 25 pc) from *Gaia* eDR3. No correction for reddening is necessary at this distance limit.
These corrections are to be applied at the discretion of the user, when deriving synthetic G-RP colour values for more distant objects from *Gaia* eDR3 catalogue.



### Acknowledgement:

if your paper uses results obtained with this code, please cite [Golovin et al. 2021, A&A, [...]]().

If you have any questions and/or comments, please contact me at `agolovin (@) lsw (dot) uni-heidelberg (dot) de`.

### A short appetizer with a few illustrative examples:

Before | After
------------ | -------------
![](/plots/20mas_HRD_obs.png) | ![](/plots/20mas_HRD_synth.png)



 ![](/plots/20mas_blended_HRD_o_c_colourcoded.png)

