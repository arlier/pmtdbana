for thr potted PMTs, we are interested in the potential change of PDE, DCR, rise time, fall time , FWHM, Gain, amplitude,HV,PV, res,sn
the strategy to analyze potted PMTs

1. get the (unique)list of potted PMTs.
2. found the potted test result(skip if not pass)
3. found the bare test result  (passed by default)


use python dictionary to store the index
the index= [PMTSN,potted_test_date,bare_test_date]

pmttest.getpottetdpde(pmtsn)


