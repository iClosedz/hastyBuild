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

# Checkout desired branch and install dependencies
process = subprocess.Popen(["git", "checkout","dev-0.3"], stdout=subprocess.PIPE)
print process.communicate()[0]

print '... Checking dependencies ...'
process = subprocess.Popen(["npm", "install"], stdout=subprocess.PIPE)
print process.communicate()[0]

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
os.chdir(buildPath)
prefix = 'popcorn_'+datetime.datetime.now().strftime("%Y%m%d")+'_'
print '... Compressing ...'
print '=> Mac'
process = subprocess.Popen(["zip","-r", prefix+'mac', 'mac'], stdout=subprocess.PIPE)
print process.communicate()[0]

print '... Compressing ...'
print '=> Windows'
process = subprocess.Popen(["zip","-r", prefix+'win', 'win'], stdout=subprocess.PIPE)
print process.communicate()[0]

print '... Compressing ...'
print '=> Linux32'
process = subprocess.Popen(["zip","-r", prefix+'linux32', 'linux32'], stdout=subprocess.PIPE)
print process.communicate()[0]

print '... Compressing ...'
print '=> Linux64'
process = subprocess.Popen(["zip","-r", prefix+'linux64', 'linux64'], stdout=subprocess.PIPE)
print process.communicate()[0]

# Upload to Mega via API ?

# Update website ?

# Print commit shortened hash
process = subprocess.Popen(["git","log","--pretty=format:'%h'","-n 1"], stdout=subprocess.PIPE)
print 'Commit Shortened Hash : '+process.communicate()[0]

print '-- Ending --'
sys.exit(0)


