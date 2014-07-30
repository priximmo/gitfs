from .view import View

from errno import ENOENT
from stat import S_IFDIR

from gitfs import  FuseMethodNotImplemented, FuseOSError
from log import log


class HistoryIndexView(View):

    def getattr(self, path, fh=None):
        '''
        Returns a dictionary with keys identical to the stat C structure of
        stat(2).

        st_atime, st_mtime and st_ctime should be floats.

        NOTE: There is an incombatibility between Linux and Mac OS X
        concerning st_nlink of directories. Mac OS X counts all files inside
        the directory, while Linux counts only the subdirectories.
        '''

        if path != '/':
            raise FuseOSError(ENOENT)
        return dict(st_mode=(S_IFDIR | 0755), st_nlink=2)


    def opendir(self, path):
        return 0

    def releasedir(self, path, fi):
        pass

    def access(self, path, amode):
        log.info('%s %s', path, amode)
        return 0

    def readdir(self, path, fh):
        return ['.', '..', 'commits everywhere']