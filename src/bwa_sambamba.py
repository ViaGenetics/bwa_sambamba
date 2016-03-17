#!/usr/bin/env python
# bwa_sambamba 0.0.1
# Generated by dx-app-wizard.
#
# Basic execution pattern: Your app will run on a single machine from
# beginning to end.
#
# See https://wiki.dnanexus.com/Developer-Portal for documentation and
# tutorials on how to modify this file.
#
# DNAnexus Python Bindings (dxpy) documentation:
#   http://autodoc.dnanexus.com/bindings/python/current/

import os
import dxpy
import logging
import time


logger = logging.getLogger(__name__)
logger.addHandler(dxpy.DXLogHandler())
logger.propagate = False


try:
    from dx_applet_utilities import common_job_operations as dx_utils, manage_command_execution as dx_exec, prepare_job_resources as dx_resources
except ImportError:
    logger.error("Make sure to add the dx_applet_utilities to execDepends in dxapp.json!")
    sys.exit(1)


@dxpy.entry_point("main")
def main(reads_1, reference, reference_index, read_group_sample,
    read_group_platform, read_group_platform_unit, read_group_library,
    advanced_bwa_options, loglevel, reads_2=None,
    advanced_sambamba_view_options=None, advanced_sambamba_sort_options=None,
    advanced_sambamba_markdups_options=None,
    advanced_sambamba_flagstat_options=None):

    """This is a dx applet that runs on the DNAnexus platform.

    :param: `reads_1`:
    :param: `reference`:
    :param: `reference_index`:
    :param: `read_group_sample`:
    :param: `read_group_platform`:
    :param: `read_group_platform_unit`:
    :param: `read_group_library`:
    :param: `advanced_bwa_options`:
    :param: `loglevel`:
    :param: `reads_2`:
    :param: `advanced_sambamba_view_options`:
    :param: `advanced_sambamba_sort_options`:
    :param: `advanced_sambamba_markdups_options`:
    :param: `advanced_sambamba_flagstat_options`:
    :returns: This will return an dx object with output generated. This is
        actually taken care of by dxpy client libraries.
    """

    # The following line(s) initialize your data object inputs on the platform
    # into dxpy.DXDataObject instances that you can start using immediately.

    reads_1 = [dxpy.DXFile(item) for item in reads_1]
    if reads_2 is not None:
        reads_2 = [dxpy.DXFile(item) for item in reads_2]
    reference = dxpy.DXFile(reference)
    reference_index = dxpy.DXFile(reference_index)

    # The following line(s) download your file inputs to the local file system
    # using variable names for the filenames.

    dxpy.download_dxfile(reference.get_id(), "reference")

    dxpy.download_dxfile(reference_index.get_id(), "reference_index")
    for i, f in enumerate(reads_1):
        dxpy.download_dxfile(f.get_id(), "reads_1-" + str(i))
    if reads_2 is not None:
        for i, f in enumerate(reads_2):
            dxpy.download_dxfile(f.get_id(), "reads_2-" + str(i))

    # Fill in your application code here.

    # The following line(s) use the Python bindings to upload your file outputs
    # after you have created them on the local file system.  It assumes that you
    # have used the output field name for the filename for each output, but you
    # can change that behavior to suit your needs.

    download_quality_metrics = dxpy.upload_local_file("download_quality_metrics")

    # The following line fills in some basic dummy output and assumes
    # that you have created variables to represent your output with
    # the same name as your output fields.

    output = {}
    output["output_markdups_bams"] = [dxpy.dxlink(item) for item in output_markdups_bams]
    output["output_cram_file_archive"] = [dxpy.dxlink(item) for item in output_cram_file_archive]
    output["download_quality_metrics"] = dxpy.dxlink(download_quality_metrics)

    return output

dxpy.run()
