import numpy as np

def convert_surv_label_structarray(surv_label):
    """
    Convert a normal array of survival labels to structured array. A structured
    array containing the binary event indicator as first field, and time of
    event or time of censoring as second field.

    Parameters
    ----------
    surv_label :  `np.ndarray`, shape=(n_samples, 2)
        Normal array of survival labels

    Returns
    -------
    surv_label_structarray : `np.ndarray`, shape=(n_samples, 2)
        Structured array of survival labels
    """
    surv_label_structarray = []
    n_samples = surv_label.shape[0]

    for i in range(n_samples):
        surv_label_structarray.append((bool(surv_label[i, 1]), surv_label[i, 0]))

    surv_label_structarray = np.rec.array(surv_label_structarray,
                                          dtype=[('indicator', bool),
                                                 ('time', np.float32)])

    return surv_label_structarray