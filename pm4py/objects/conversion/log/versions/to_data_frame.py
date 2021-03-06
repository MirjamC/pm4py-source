import pandas as pd

from pm4py.objects.log import log as log_instance
from pm4py.objects.conversion.log.variants import to_event_stream
import deprecation

@deprecation.deprecated(deprecated_in='1.3.0', removed_in='2.0.0', current_version='',
                        details='conversion versions are deprecated; use conversion variants instead')
def apply(log, parameters=None):
    """
    Converts a provided event log object into a Pandas dataframe. As a basis, an EventStream object is used.
    In case an EventLog object is given, it is first converted to an EventStream object.
    Within the conversion, the order is not changed, i.e., the order imposed by the iterator is used.

    Parameters
    -----------

    log :class:`pm4py.log.log.EventLog`
        Event log object, can either be an EventLog object, EventStream Object or Pandas dataframe

    parameters :class:`dict`
        Parameters of the algorithm

    Returns
    -----------
    df
        Pandas dataframe
    """
    # if parameters is None:
    #    parameters = {}
    if isinstance(log, pd.core.frame.DataFrame):
        return log
    if type(log) is log_instance.EventLog:
        log = to_event_stream.__transform_event_log_to_event_stream(log)
    transf_log = [dict(x) for x in log]
    df = pd.DataFrame.from_dict(transf_log)

    return df
