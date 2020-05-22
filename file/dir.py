# (C) 2019-2020 lifegpc
# This file is part of bili.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from file.info import getinfox,printinfo
from os.path import exists,abspath
from os import listdir
from file.str import width
def getinfod(filelist) :
    "从listd获得的列表得到信息"
    j=1
    ar=[]
    for i in filelist :
        r=getinfox(i,j)
        if r!=-1 :
            j=j+1
            ar.append(r)
    return ar
def printinfod(filelist) :
    "打印整个filelist"
    m=maxwidth(filelist)
    j=1
    print('序号\t文件名\t',end='')
    while m > 8 :
        print('\t',end='')
        m=m-8
        j=j+1
    print('类型\t上次访问时间\t\t创建时间\t\t上次修改时间\t\t文件大小')
    for i in filelist :
        printinfo(i,j*8)
def listd(l='.'):
    '获取列表'
    d=listdir(l)
    r=[]
    for i in d :
        if l!='.' :
            r.append({'a':abspath('%s/%s' % (l,i)),'f':i})
        else :
            r.append({'a':abspath(i),'f':i})
    return r
def maxwidth(l) :
    m=0
    for i in l:
        n=width(i['f'])
        if n>m :
            m=n
    return m
def listc(l,s=0,e='True') :
    "截取listinfo中的一部分"
    if e=='True' :
        e=len(l)
    r=[]
    j=1
    for i in l[s:e] :
        i['x']=j
        r.append(i)
        j=j+1
    return r