%global tl_name scripture
%global tl_revision 79351

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	A LaTeX style for typesetting Bible quotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/scripture
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scripture.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scripture.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scripture.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The scripture package provides a set of macros for typesetting
quotations from the Bible. It provides many features commonly seen in
Bibles such as dropped text for chapter numbers, superscripts for verse
numbers, indented lines for poetry sections, narrow sections and hanging
paragraphs. A reference for the quotation can optionally be added.

