import xarray as xr
import pandas as pd

# Load the NetCDF file
file_path = "../../data/time_series/8518750.nc"
ds = xr.open_dataset(file_path)

# Convert 'date' from string to datetime64
ds["date"] = pd.to_datetime(ds["date"].values, format="%Y-%m-%d %H:%M")

# Rename 'date' to 'time' (if required for compatibility)
# ds = ds.rename({"date": "time"})

# Verify the conversion
print(ds["date"].values[:10])  # Print first 10 timestamps
print("Dataset time range:", ds["date"].min().values, "to", ds["date"].max().values)

output_file = "../../data/time_series/8518751.nc"
ds.to_netcdf(output_file)

print(f"Fixed dataset saved to: {output_file}")
