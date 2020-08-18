def annualize_rets(r, periods_per_year):
    """
    Returns compounded growth with rate r
    """
    compounded_growth = (1+r).prod()
    n_periods = r.shape[0]
    return compounded_growth**(periods_per_year/n_periods)-1

def annualize_vol(r, periods_per_year):
    """
    Returns annual volatility with rate r
    """
    return r.std()*(periods_per_year**0.5)

def sharpe_ratio(r, rfr=0.025, periods_per_year):
    """
    Returns annualized sharpe ratio with rate r
    """
    rf_per_period = (1+rfr)**(1/periods_per_year)-1
    excess_ret = r - rf_per_period
    annual_rets = annualize_rets(excess_ret, periods_per_year)
    annual_vol = annualize_vol(r, periods_per_year)
    return annual_rets/annual_vol
