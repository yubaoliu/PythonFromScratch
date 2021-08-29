import os
import tempfile

# define the access rights
access_rights = 0o755

print("===========================")
print("Creating a Directory ")
# define the name of the directory to be created
path = "/tmp/year"
print("Create directory: %s" % path)
try:
    os.mkdir(path, access_rights)
except OSError as error:
    print(error)
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)

print("===========================")
print("Creating a Directory with Subdirectories")
path = "/tmp/year/month/week/day"
print("Create directory (mkdir -p): %s" % path)
try:
    os.makedirs(path, access_rights)
except OSError as error:
    print(error)
    print("Creation of the directory %s failed" % path)
else:
    print("Successfully created the directory %s" % path)


# print("===========================")
# print("create a temporary directory")
# with tempfile.TemporaryFile() as directory:
#     print('The created temporary directory is %s' % directory)

print("===========================")
path = "/tmp/year"
print("Delete directory: %s" % path)
try:
    if os.path.exists(path):
        os.rmdir(path)
except OSError as error:
    print(error)
    print("Deletion of the directory %s failed" % path)
else:
    print("Successfully deleted the directory %s" % path)


print("===========================")
path = "/tmp/year"
print("Simple method: %s" % path)
print("Delete directory: %s" % path)
if os.path.exists(path):
    os.system("rm -r /tmp/year")

