import sublime
import sublime_plugin

# Search dirs
# /home/todd/Downloads/Sublime Text 2/Pristine Packages/,/home/todd/.config/sublime-text-2/Packages

# TODO: Definitely use code from Default/Find in Files.sublime-menu
# We are already using Default/Find Results.hidden-tmLanguage for Default.sublime-keymap insights


# Command to delete a line (used by Find Results)
class FindPlusPlusDeleteLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Note: This is blantantly ripped from Packages/Default/Delete Line.sublime-macro
        # [
        #     {"command": "expand_selection", "args": {"to": "line"}},
        #     {"command": "add_to_kill_ring", "args": {"forward": true}},
        #     {"command": "left_delete"}
        # ]

        # Localize view
        view = self.view

        # TODO: If this is a file name we are deleting (e.g. start of a set of results), delete them all

        # Expand selection to line, include line feed, delete lines
        view.run_command("expand_selection", {"to": "line"})
        view.run_command("add_to_kill_ring", {"forward": True})
        view.run_command("left_delete")


# Class to make Find matching easier
class Finder:
    def __init__(self, settings):
        # Save settings for later
        # TODO: We might just read directly from settings?
        self.settings = settings

    def find(self, view):
        pass


# DEV: On focus of a window, give me an error message
class FindPlusPlus(sublime_plugin.EventListener):
    def on_load(self, view):
    #     # sublime.error_message('activated')
    #     sublime.error_message('loaded')
        print "loaded"
        pass

    def on_modified(self, view):
    #     sublime.error_message('modified')
        print "modified"
        print("size", view.size())
        # print("name", view.name())
        # print("file_name", view.file_name())
        # print("is_loading", view.is_loading())
        # print("is_dirty", view.is_dirty())
        # print view.settings().get('syntax')
        # print view.window().views()
        # print view.is_read_only()
        # print view.id()
        # print view.buffer_id()

    # def on_activated(self, view):
    #     sublime.error_message('activated')
    #     pass
        # # If this is a FindPlusPlus.py
        # file_name = view.file_name() or ''
        # if file_name.endswith('FindPlusPlus.py'):
        #     print "focus gained"
        #     # now
        #     # FindNow()
        #     # matches = [sublime.Region(646, 649), sublime.Region(1066, 1069)]
        #     # print matches
        #     FindResults('hey')
        #     pass


# Class for search panel
class FindPanel:
    def __init__(self):
        pass

# TODO: Sooner rather than later, deletion of row via 'delete'

# DEV: Proof of concept for getting search results from page
class FindNow:
    def __init__(self):
        # Get the active view
        view = self.get_active_view()

        # Get search results
        results = view.find_all('now')

        # List of sublime.regions =)
        print results
        print results.length


    def get_window(self):
        return sublime.active_window()

    def get_active_view(self):
        window = self.get_window()
        return window.active_view()


# Class to handle find results
class FindResults:
    def __init__(self, settings):
        # TODO: All actions inside of init should be methods themself?
        # Get the window
        window = self.get_window()
        self.window = window

        # Save name of output panel
        panel_name = 'FindPPResults'
        self.panel_name = panel_name

        # Get a panel
        results = window.get_output_panel(panel_name)
        self.results = results

        # Show the panel
        self.show()

        # Write out some content
        self.write('hello world')
        pass

    def get_window(self):
        return sublime.active_window()

    def output_name(self):
        return 'output.' + self.panel_name

    def show(self):
        # Open the panel
        output_name = self.output_name()
        self.window.run_command('show_panel', {'panel': output_name})

    def hide(self):
        # Hide the panel
        output_name = self.output_name()
        self.window.run_command('hide_panel', {'panel': output_name})

    def write(self, content):
        # Grab the result panel
        results = self.results

        # Begin editing it
        edit = results.begin_edit()

        # Insert some text
        results.insert(edit, 0, content)

        # Stop editing
        results.end_edit(edit)
