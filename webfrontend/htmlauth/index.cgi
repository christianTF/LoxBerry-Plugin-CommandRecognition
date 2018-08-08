#!/usr/bin/perl

use LoxBerry::Web;
my $plugintitle = "Command Recognition";
my $helplink = "http://www.loxwiki.eu:80/x/2wzL";
# my $helptemplate = "help.html";

LoxBerry::Web::lbheader($plugintitle, $helplink, $helptemplate);

my $template = HTML::Template->new(
    filename => "$lbptemplatedir/comrec.html",
    global_vars => 1,
    loop_context_vars => 1,
    die_on_bad_params => 0,
);

print $template->output();

LoxBerry::Web::lbfooter();
