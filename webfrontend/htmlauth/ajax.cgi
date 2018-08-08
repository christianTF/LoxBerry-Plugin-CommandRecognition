#!/usr/bin/perl

use CGI;
use warnings;
use strict;
use LWP::Simple;

our $cgi = CGI->new;
$cgi->import_names('R');

if ($R::action eq "request") {
	my $contents = get($R::url);
	print $cgi->header('text/html');
	print $contents;
	exit;

}
