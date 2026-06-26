# UK Climate Analysis

A data-driven challenge to the "new norm" framing of UK climate change.

## What this is about

I want to be clear about who this project is and isn't aimed at. There are a lot of people who understand that data can be used to explain things we observe. I'm one of those people. I know how to interrograte data and torture it until it tells us everything it knows. I also know when I don't have enough data to answer questions. But I'm also fully aware that there are certain groups of people who will not accept facts no matter what you present them with. This is true in many of the fields I work in and study in. 

This is not aimed at climate change deniers. Climate change is real, it is caused by human activity, and engaging with people who dispute that is not a productive use of anyone's time. That argument is settled in the science.

This project is aimed at something more insidious: the casual minimisation of climate change by people who broadly accept it's happening but consistently understate what it means. The TV weather presenters who describe record-breaking summer temperatures as the "new norm". The commentators who frame climate change as a matter of warmer holidays and remind people to stay hydrated. The well-meaning people who have absorbed the message that things are getting warmer but concluded that we're simply adjusting to a new stable state. One of the catalysts for this work are the stories in the UK news recently (late June 2026) saying how the UK has broken its June heat record three days in a row in the same tone that is used when a British person breaks the world record for balancing biscuits on their head.

That framing is wrong. And it matters that it's wrong, because it implies adaptation is sufficient — that we're moving to a new normal we can plan around — when the evidence points toward something fundamentally different.

The data does not show a step change to a stable warmer state. It shows an accelerating trajectory. There is a significant difference between "it's going to be warmer every summer" and "it's going to be warmer every summer than it was the year before, and that rate of warming is itself increasing." The first is a new norm. The second is not.

This project makes that argument with 190 years of publicly available UK climate data.

---

## The data

All data comes from the Met Office HadUK-Grid regional climate series — the same observational record the Met Office uses for operational climate monitoring.

**Source:** https://www.metoffice.gov.uk/research/climate/maps-and-data/uk-and-regional-series

**Variables:**
| Variable | Description | Record starts |
|---|---|---|
| `Tmean` | Mean air temperature (°C) | 1884 |
| `Tmax` | Maximum air temperature (°C) | 1884 |
| `Tmin` | Minimum air temperature (°C) | 1884 |
| `Rainfall` | Total precipitation (mm) | 1836 |
| `Sunshine` | Sunshine duration (hours) | 1910 |
| `AirFrost` | Days of air frost | 1931 |
| `Raindays1mm` | Days with rainfall ≥ 1mm | 1891 |

**Coverage:** UK, England, Scotland, Wales, Northern Ireland, and nine English sub-regions — 17 geographies in total, 119 files, 280,041 data points.

Download instructions are in `data/raw/README.md`.

---

## What the analysis finds

### The warming rate has nearly tripled

Across the full 141-year record, UK mean annual temperature has risen at approximately 0.12°C per decade. In the period from 1991 to 2025, the rate is 0.33°C per decade — nearly three times faster. The rolling trend analysis shows the slope rising since the 1980s and remaining elevated. Every time window fitted to the data, including the most recent 15 years, shows a statistically significant positive warming trend.

The slope has not flattened.

### This is not a warmer summers story

All four seasons are warming. In the recent period, **winter is warming faster than summer**. Every month of the year shows a positive warming trend. No region of the UK is exempt. The "warmer summers" framing is not just incomplete — it describes the least alarming part of what is happening and ignores the rest.

### Variability is increasing alongside the mean

A genuine new norm would imply a higher mean but similar predictability. Year-to-year temperature variability has increased in recent decades. The climate is not just warmer — it is less stable. The swings are getting bigger as the average rises.

### Multiple indicators are moving simultaneously

Frost days are declining. Rainfall is becoming more intense - the same annual totals falling in fewer, heavier events. Sunshine hours are shifting. These are consistent signatures of a system under sustained pressure, not a system settling into a new equilibrium.

### The +2°C threshold arrives in the late 2030s

Under the current rate of warming, the UK mean annual temperature trend line crosses +2°C above its 1961–1990 baseline in the late 2030s. Individual years have already reached +1.5°C above baseline — 2022, 2023, 2024 and 2025 are all in the top five on record. The 15 warmest years in the 141-year record are almost entirely post-2000.

---

## What this analysis cannot claim

This is not a climate model. It does not incorporate atmospheric physics, emissions pathways, or feedback loops. The projections are extrapolations of the observed trend — statements of the form *if the current rate continues, here is where we end up* — not forecasts.

The attribution question (how much of the observed change is human-caused versus natural variability) has been answered comprehensively by the IPCC and by the Met Office's own UKCP18 projections. This analysis is consistent with those assessments and contributes an independently reproducible view of the observed record.

---

## Structure

```
notebooks/
  01_data_acquisition.ipynb       Load all 119 files, produce clean dataset
  02_trend_analysis.ipynb         Is the rate of warming accelerating? Yes.
  03_regional_and_seasonal.ipynb  All seasons, all regions — not just summer
  04_projection.ipynb             What the current trajectory implies
  05_synthesis.ipynb              The complete argument in one place

data/
  raw/       119 Met Office .txt files (not committed — see data/raw/README.md)
  processed/ climate_series.csv produced by notebook 01 (not committed)

outputs/     Charts generated by the notebooks
```

---

## Reproducing the analysis

```bash
git clone git@github.com:stetho/uk-climate-analysis.git
cd uk-climate-analysis
pip install -r requirements.txt
# Download raw data files per data/raw/README.md
jupyter notebook
```

Run notebooks in order. Each reads from `data/processed/` and the first notebook produces that file from the raw data.

---

## Author

Steve Thompson — [stetho.me](https://stetho.me) | [GitHub](https://github.com/stetho)

*Data source: Met Office HadUK-Grid regional climate series, available under Open Government Licence.*
