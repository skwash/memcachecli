#!/usr/bin/env python

import os
import cmd
import memcache
import readline
import argparse

historyPath = os.path.expanduser("~/.memcache_history")


class InteractiveMemcache(cmd.Cmd):
    """Interpret and execute memcached protocol commands."""

    mc = None
    host = None

    def connect(self):
        self.mc = memcache.Client([self.host], debug=0)

        #print "Connected to memcached ({})".format(self.host)
        self.prompt = "{}> ".format(self.host)

    def do_connect(self, line):
        """Connect to memcache server."""
        self.connect()
        #print self.mc

    def do_get(self, line):
        """Get a key's value from memcache."""
        # get KEY

        if not self.mc:
            self.connect()

        key = line.split()[0]

        resp = self.mc.get(line)
        print "GET", key
        print resp

    def do_delete(self, line):
        """Delete a key from memcache."""
        # delete KEY

        if not self.mc:
            self.connect()

        key = line.split()[0]
        resp = self.mc.delete(key)
        print "DELETE", key
        print resp

    def do_set(self, line):
        """Set a key/value"""
        #set KEY VALUE

        if not self.mc:
            self.connect()

        key, val = line.split(' ', 1)
        resp = self.mc.set(key, val)
        print "SET", key, val
        print resp

    def go_quit(self, line):
        """Quit."""
        readline.write_history_file(historyPath)
        print ""
        return True

    def do_EOF(self, line):
        readline.write_history_file(historyPath)
        print ""
        return True


def main():

    parser = argparse.ArgumentParser(description='Interactive memcache client.')
    parser.add_argument('host', metavar='HOSTNAME', default='localhost',
                        help='Server to connect to.')
    parser.add_argument('--port', metavar='port',
                        help='Server port.', default=11211)

    args = parser.parse_args()

    if os.path.exists(historyPath):
        readline.read_history_file(historyPath)

    i = InteractiveMemcache()
    i.host = '{}:{}'.format(args.host, args.port)
    i.prompt = "No server(s)> "
    i.cmdloop()
