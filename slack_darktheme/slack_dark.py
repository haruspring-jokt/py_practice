import sys

class File_writer:

    def execute(self, path):
        file = open(path, 'a')  # 追加書き込みモード
        string = """
        document.addEventListener('DOMContentLoaded', function() {
    $.ajax({
    url: 'https://cdn.rawgit.com/laCour/slack-night-mode/master/css/raw/black.css',
        success: function(css) {
                $("<style></style>").appendTo('head').html(css);
            }
        });
    });
    """
        file.writelines(string)
        file.close



args = sys.argv

print('-------------------------------------------------------------')
print('このファイルに追記します: ' + args[1])
print('-------------------------------------------------------------')
writer = File_writer()
writer.execute(args[1])

