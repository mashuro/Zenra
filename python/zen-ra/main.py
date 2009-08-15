#/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from google.appengine.ext.webapp import WSGIApplication
from google.appengine.ext.webapp.util import run_wsgi_app


def main():
    logging.getLogger().setLevel(logging.DEBUG)
    application = WSGIApplication([
            ], debug = True)
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
