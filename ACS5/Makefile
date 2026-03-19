SHELL := /bin/bash
include ../Makevars

OUTPUTS := $(foreach year,$(ACS5_YEARS),$(foreach tab,$(ACS5_TABLES), $(tab)__$(year).csv.gz))

.PHONY: all state county tract block_group clean

all: $(OUTPUTS)

state:
	$(MAKE) -C state

county:
	$(MAKE) -C county

tract:
	$(MAKE) -C tract

block_group:
	$(MAKE) -C block_group

%.csv.gz: %.csv
	gzip -n -f -9 $<

%.csv: ../utilities/stacktogether.R | state county tract block_group
	$(RSCRIPTVANILLA) $< $*

clean:

# ------------------------------------------------------------------------------
