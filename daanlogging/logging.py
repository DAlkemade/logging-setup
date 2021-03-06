import logging
import os


def set_up_root_logger(application_tag: str, logs_dir: str) -> None:
    """Set up root logger.

    :param application_tag: tag for log filename
    :param logs_dir: directory to save logs in
    """
    if not os.path.exists(logs_dir):
        print("LOGS DIR DOES NOT EXIST")
        raise ValueError("Logs dir does not exist")
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename=os.path.join(logs_dir, f'{application_tag}.log'),
                        filemode='w')
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
