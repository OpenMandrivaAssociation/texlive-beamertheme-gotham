%global tl_name beamertheme-gotham
%global tl_revision 78692

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2.5.a
Release:	%{tl_revision}.1
Summary:	A modern, minimal-ish, versatile and extendable yet robust theme for Beamer
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamertheme-gotham
License:	lppl1.3c cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-gotham.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-gotham.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-gotham.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a modern, minimal-ish, versatile, LaTeX3 and
extendable yet robust Beamer theme with some lines of code gathered or
borrowed from other themes. It uses the l3build system to both build and
verify (Test-Driven Development) the delivered code. "Gotham" tries to
bring higher flexibility thanks to LaTeX3 implementation on top of the
good-looking Metropolis theme.

