echo -1 >/etc/acq400/0/OVERSAMPLING
export EPICS_CA_MAX_ARRAY_BYTES=500000
export IOC_POSTINIT=/mnt/local/sysconfig/set_dt_test_role

