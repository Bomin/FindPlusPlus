import sublime
import sublime_plugin


# Command to delete a line (used by Find Results)
class FindppDeleteLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Localize view
        view = self.view

        # Open an edit
        edit = view.begin_edit()

        # For each region in selection
        for region in view.sel():
            # Get the region of the line
            line = view.line(region)

            # TODO: This might get annoying without a reverse sort
            # Delete the line
            view.erase(edit, line)

        # Stop the edit
        view.end_edit(edit)

        # TODO: Expand region to line
        # TODO: Delete line
        # Note: We could use Packages/Default/Delete Line.sublime-macro but it is a macro
        print "test"


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
    def on_activated(self, view):
        pass
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
