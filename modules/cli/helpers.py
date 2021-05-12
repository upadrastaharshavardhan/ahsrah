class Helpers():

    @staticmethod
    def _general_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        clear/cls               clear the ahsrah screen
        use       <Variable>    Use an variable.
        info      <Variable>    Get information about an available variable.
        set <variable> <value>  Sets a context-specific variable to a value to use while using ahsrah.
        variables               Prints all previously specified variables.
        banner                  Display banner.
        history                 Display command-line most important history from the beginning.
        makerc                  Save command-line history to a file.
        exec       <command>    Execute a system command without closing the ahsrah-mode
        exit/quit               Exit the ahsrah-mode
        """)

    @staticmethod
    def _url_action_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        timeout                 set timeout
        ports                   scan ports
        domain                  get domains & sub domains
        cms info                get cms info (version , user ..)
        web info                get web info
        dump dns                dump dns get sub domains [mx-server..]
        run exploit             run exploits corresponding to cms
        clear/cls               clear the ahsrah screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)

    # dorks - command helpers.

    @staticmethod
    def _dorks_action_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        list                    list dorks
        set dork                set exploit name
        clear/cls               clear the ahsrah screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        exec       <command>    Execute a system command without closing the ahsrah-mode
        back                    move back from current context
        """)

    @staticmethod
    def _dorks_setdork_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        pages                   set num page
        output                  output file.
        run                     search web with specified dork
        clear/cls               clear the ahsrah screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        exec       <command>    Execute a system command without closing the ahsrah-mode
        back                    move back from current context
        """)

    @staticmethod
    def _dorks_setdork_page_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        output                  output file.
        run                     search web with specified dork
        clear/cls               clear the ahsrah screen
        exec       <command>    Execute a system command without closing the ahsrah-mode
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)

    @staticmethod
    def _dorks_setdork_output_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        pages                   set num page
        run                     search web with specified dork
        exec       <command>    Execute a system command without closing the ahsrah-mode
        clear/cls               clear the ahsrah screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)

    @staticmethod
    def _dorks_setdork_page_output_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        run                     search web with specified dork
        clear/cls               clear the ahsrah screen
        exec       <command>    Execute a system command without closing the ahsrah-mode
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)
© 2021 GitHub, Inc.
