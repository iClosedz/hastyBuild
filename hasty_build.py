#!/usr/bin/python
import os
import sys
import commands
import subprocess
import shutil
import datetime

# Check Valid arguments
if len(sys.argv) == 1:
	print 'Need folder'
	sys.exit(2)

# Check Valid Path
folderPath = str(sys.argv[1])
if not os.path.exists(folderPath):
	print 'Invalid folder'
	sys.exit(2)

# Delete previous builds if any
buildPath = folderPath+'/build/releases/PopCorn-Time'
if os.path.exists(buildPath):
	print '-- Deleting previous builds --'
	shutil.rmtree(buildPath)

# Move into folder
os.chdir(folderPath)

# Pull for updates
print '... Pulling ...'
process = subprocess.Popen(["git", "pull"], stdout=subprocess.PIPE)
print process.communicate()[0]

# Building
print '... Building ...'
print '=> Mac'
process = subprocess.Popen(["grunt", "build", "--platforms=mac"], stdout=subprocess.PIPE)
print process.communicate()[0]

print '=> Windows'
process = subprocess.Popen(["grunt", "build", "--platforms=win"], stdout=subprocess.PIPE)
print process.communicate()[0]

print '=> Linux32'
process = subprocess.Popen(["grunt", "build", "--platforms=linux32"], stdout=subprocess.PIPE)
print process.communicate()[0]

print '=> Linux64'
process = subprocess.Popen(["grunt", "build", "--platforms=linux64"], stdout=subprocess.PIPE)
print process.communicate()[0]

# Compressing
prefix = buildPath+'/ptc_'+datetime.datetime.now().strftime("%Y%m%d")+'_'
print '... Compressing ...'
print '=> Mac'
process = subprocess.Popen(["zip", prefix+'mac', buildPath+'/mac'], stdout=subprocess.PIPE)
print process.communicate()[0]

print '... Compressing ...'
print '=> Windows'
process = subprocess.Popen(["zip", prefix+'win', buildPath+'/win'], stdout=subprocess.PIPE)
print process.communicate()[0]

print '... Compressing ...'
print '=> Linux32'
process = subprocess.Popen(["zip", prefix+'linux32', buildPath+'/linux32'], stdout=subprocess.PIPE)
print process.communicate()[0]

print '... Compressing ...'
print '=> Linux64'
process = subprocess.Popen(["zip", prefix+'linux64', buildPath+'/linux64'], stdout=subprocess.PIPE)
print process.communicate()[0]

# Upload to Mega via API ?

# Update website ?

print '-- Ending --'
sys.exit(0)


